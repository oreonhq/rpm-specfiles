Name:           cjose
Version:        0.6.2.2
Release:        10%{?dist}
Summary:        C library implementing the Javascript Object Signing and Encryption (JOSE)

License:        MIT
URL:            https://github.com/OpenIDC/cjose
Source0:        https://github.com/OpenIDC/cjose/releases/download/v%{version}/cjose-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 2de8652b23ee3e15398176e8b2aaa513aa89635368f2748fbc304f8aefe910a4
%global source0_file cjose-0.6.2.2.tar.gz
# oreon url source checksums end

BuildRequires:  gcc
BuildRequires:  doxygen
BuildRequires:  openssl-devel
BuildRequires:  jansson-devel
BuildRequires:  check-devel
BuildRequires: make

%description
Implementation of JOSE for C/C++


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/cjose-0.6.2.2.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "2de8652b23ee3e15398176e8b2aaa513aa89635368f2748fbc304f8aefe910a4" || { echo "oreon: Source0 SHA256 mismatch for cjose-0.6.2.2.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -n %{name}-%{version} -p1

%build
%configure
%make_build


%install
%make_install
find %{buildroot} -name '*.a' -exec rm -f {} ';'
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%ldconfig_scriptlets


%check
make check || (cat test/test-suite.log; exit 1)

%files
%license LICENSE
%doc CHANGELOG.md README.md
%doc /usr/share/doc/cjose
%{_libdir}/*.so.*


%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/cjose.pc


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6.2.2-10
- Prepare for Oreon 11 (RP1)
