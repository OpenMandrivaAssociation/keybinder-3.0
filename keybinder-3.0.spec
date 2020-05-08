%define oname		keybinder

%define major           0
%define api		3.0
%define gmajor		3.0
%define libname         %mklibname %{oname} %{api} %{major}
%define girname		%mklibname %{oname}-gir %{gmajor}
%define develname       %mklibname -d %{oname} %{api}

Name:           keybinder3.0
Version:        0.3.2
Release:        2
Summary:        A library for registering global keyboard shortcuts
License:        X11 License
Group:          Development/GNOME and GTK+
URL:            https://github.com/kupferlauncher/keybinder
Source0:        https://github.com/kupferlauncher/keybinder/releases/download/%{oname}-%{api}-v%{version}/%{oname}-%{api}-%{version}.tar.gz

BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)

%description
%{name} is a library for registering global keyboard shortcuts. Keybinder
works with GTK3-based applications using the X Window System.

%package -n %{libname}
Group:          System/Libraries
Summary:        %{name} library package

%description -n %{libname}
Shared libraries for %{name}.

%package -n %{girname}
Summary:        GObject Introspection interface description for %{name}
Group:          System/Libraries
Requires:       %{libname} = %{version}-%{release}

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{develname}
Group:          Development/GNOME and GTK+
Summary:        %{name} developement files
Provides:       %{name}-devel = %{version}-%{release}
Requires:       %{libname} = %{version}
Requires:	%{girname} = %{version}

%description -n %{develname}
This package contains header files needed when building applications based on
%{name}.

%prep
%setup -q -n %{oname}-%{api}-%{version}

%build
%configure \
	--disable-static \
	--enable-introspection=yes
%make_build

%install
%make_install

# don't ship .la
find %{buildroot} -name '*.la' -delete

%files
%doc NEWS AUTHORS README

%files -n %{libname}
%{_libdir}/libkeybinder-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Keybinder-%{gmajor}.typelib

%files -n %{develname}
%doc %{_datadir}/gtk-doc/html/%{oname}-%{api}
%{_includedir}/%{oname}-%{api}
%{_libdir}/libkeybinder-%{api}.so
%{_libdir}/pkgconfig/keybinder-%{api}.pc
%{_datadir}/gir-1.0/Keybinder-%{gmajor}.gir

