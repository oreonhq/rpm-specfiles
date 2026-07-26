%global source0_hash 823aa663fcc2f6844ae5e9ea83ceda4ed393cdb3dadefce9b3c7c41cd0f4f702

# Upstream doesn't make releases.  We have to check the code out of git.
# Use the cvc5 branch.
%global gittag   e6ac3af9c2c574498ea171c957425b407625448b
%global shorttag %{sub %{gittag} 1 7}
%global gitdate  20230627

# There are no ELF objects in this package, so turn off debuginfo generation.
%global debug_package %{nil}

Name:           symfpu
Version:        0
Release:        0.21.%{gitdate}git%{shorttag}%{?dist}
Summary:        An implementation of IEEE-754 / SMT-LIB floating-point 

License:        GPL-3.0-or-later
URL:            https://github.com/cvc5/symfpu
VCS:            git:%{url}.git
Source:         %{url}/archive/%{gittag}/%{name}-%{shorttag}.tar.gz

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%description
SymFPU is an implementation of the SMT-LIB / IEEE-754 operations in terms of
bit-vector operations.  It is templated in terms of the bit-vectors,
propositions, floating-point formats and rounding mode types used.  This
allows the same code to be executed as an arbitrary precision "SoftFloat"
library (although it's performance would not be good) or to be used to build
symbolic representations of floating-point operations suitable for use in
"bit-blasting" SMT solvers (you could also generate circuits from them but
again, performance will likely not be good).

%package devel
Summary:        Development files for %{name}
BuildArch:      noarch
Provides:       %{name}-static = %{version}-%{release}

%description devel
This package contains header files and library links for developing
applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{gittag}

%build
# Nothing to do

%install
mkdir -p %{buildroot}%{_includedir}/%{name}
cp -a core utils %{buildroot}%{_includedir}/%{name}

%files devel
%license LICENSE
%{_includedir}/%{name}/

%changelog
%autochangelog
