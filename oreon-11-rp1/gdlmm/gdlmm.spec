%global source0_hash e280ed9233877b63ad0a0c8fb04d2c35dc6a29b3312151ee21a15b5932fef79b

%global apiver 3.0
# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           gdlmm
Version:        3.7.3
Release:        29%{?dist}
Summary:        C++ bindings for the gdl library

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.gtkmm.org/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/gdlmm/%{release_version}/gdlmm-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  glibmm24-devel
BuildRequires:  gtkmm30-devel
BuildRequires:  libgdl-devel
BuildRequires: make

%description
This package contains C++ bindings for the GNOME Development/Docking (gdl)
library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        API documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description    doc
This package contains the full API documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/*.la

%check
make check

%ldconfig_scriptlets

%files
%doc AUTHORS COPYING NEWS README
%{_libdir}/*.so.*

%files devel
%{_includedir}/gdlmm-%{apiver}/
%{_libdir}/*.so
%{_libdir}/gdlmm-%{apiver}/
%{_libdir}/pkgconfig/*.pc

%files doc
%doc %{_docdir}/gdlmm-%{apiver}/
%doc %{_datadir}/devhelp/

%changelog
%autochangelog
