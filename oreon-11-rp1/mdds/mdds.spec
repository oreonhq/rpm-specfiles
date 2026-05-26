# header-only library
%global debug_package %{nil}

%global apiversion 3.0

Name: mdds
Version: 3.0.0
Release: %autorelease
Summary: A collection of multi-dimensional data structures and indexing algorithms

License: MIT
URL: https://gitlab.com/mdds/mdds
Source0: https://gitlab.com/mdds/mdds/-/archive/%{version}/mdds-%{version}.tar.bz2
# https://gitlab.com/mdds/mdds/-/merge_requests/94
Patch0:  include.patch
# oreon url source checksums begin
%global source0_sha256 2d056dbec3a3a16c48e3451532ff53afe8fc23ed1f56bed4191197fa99a4b202
%global source0_file mdds-3.0.0.tar.bz2
# oreon url source checksums end

BuildRequires: make
BuildRequires: boost-devel
BuildRequires: gcc-c++
BuildRequires: autoconf
BuildRequires: automake

%description
%{name} is a collection of multi-dimensional data structures and
indexing algorithms.

%package devel
Summary: Headers for %{name}
BuildArch: noarch
Requires: boost-devel
Provides: %{name}-static = %{version}-%{release}

%description devel
%{name} is a collection of multi-dimensional data structures and
indexing algorithms.
 
It implements the following data structures:
* segment tree
* flat segment tree 
* rectangle set
* point quad tree
* multi type matrix
* multi type vector

See README.md for a brief description of the structures.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/mdds-3.0.0.tar.bz2; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "2d056dbec3a3a16c48e3451532ff53afe8fc23ed1f56bed4191197fa99a4b202" || { echo "oreon: Source0 SHA256 mismatch for mdds-3.0.0.tar.bz2" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p0

%build
./autogen.sh
%configure

%install
%make_install
rm -rf %{buildroot}%{_docdir}/%{name}

%check
make check %{?_smp_mflags}

%files devel
%{_includedir}/%{name}-%{apiversion}
%{_datadir}/pkgconfig/%{name}-%{apiversion}.pc
%doc AUTHORS README.md
%license LICENSE

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.0.0-1
- Prepare for Oreon 11 (RP1)
