%global source0_hash c3d23b37dfd6e39f2e09f091b77b1541fbfa17c4f0b6bf5c89baef7229080e17

Name:           libsigc++30
Version:        3.6.0
Release:        7%{?dist}
Summary:        Typesafe signal framework for C++

License:        LGPL-2.1-or-later
URL:            https://github.com/libsigcplusplus/libsigcplusplus
Source0:        https://github.com/libsigcplusplus/libsigcplusplus/releases/download/3.6.0/libsigc++-3.6.0.tar.xz

BuildRequires:  docbook-style-xsl
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libxslt
BuildRequires:  m4
BuildRequires:  meson
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl-interpreter

%description
libsigc++ implements a typesafe callback system for standard C++. It
allows you to define signals and to connect those signals to any
callback function, either global or a member function, regardless of
whether it is static or virtual.

libsigc++ is used by gtkmm to wrap the GTK+ signal system. It does not
depend on GTK+ or gtkmm.


%package        devel
Summary:        Development tools for the typesafe signal framework for C++
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains the static libraries and header files
needed for development with %{name}.


%package        doc
Summary:        Documentation for %{name}, includes full API docs
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description    doc
This package contains the full API documentation for %{name}.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n libsigc++-%{version}

chmod -x NEWS


%build
%meson -Dbuild-documentation=true
%meson_build


%install
%meson_install


%files
%license COPYING
%doc NEWS README.md
%{_libdir}/libsigc-3.0.so.0*

%files devel
%{_includedir}/sigc++-3.0/
%{_libdir}/sigc++-3.0/
%{_libdir}/pkgconfig/sigc++-3.0.pc
%{_libdir}/libsigc-3.0.so

%files doc
%doc %{_datadir}/doc/libsigc++-3.0/
%doc %{_datadir}/devhelp/


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.6.0-7
- Prepare for Oreon 11 (RP1)
