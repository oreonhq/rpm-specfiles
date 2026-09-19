%global source0_hash 7787c4609d44cb8b5c59163b941e082091fe427058c540999090e74c9545bd95

%global debug_package %{nil}

Name:           sblim-testsuite
Version:        1.3.0
Release:        35%{?dist}
Summary:        SBLIM testsuite

License:        EPL-1.0
URL:            http://sblim.wiki.sourceforge.net/
Source0:        http://downloads.sourceforge.net/sblim/%{name}-%{version}.tar.bz2
BuildArch:      noarch
BuildRequires: make
BuildRequires:      perl-generators

Requires:       perl-interpreter >= 5.6
Requires:       sblim-wbemcli >= 1.5

Patch0:         sblim-testsuite-1.3.0-perl-errors.patch
# Patch1: removes version from docdir
Patch1:         sblim-testsuite-1.3.0-docdir.patch
# Patch2: fixes unescaped left brace perl warning
Patch2:         sblim-testsuite-1.3.0-unescaped-left-brace-warning-fix.patch

%description
SBLIM automated testsuite scripts.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%autopatch -p1

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING README
%{_datadir}/%{name}
%{_localstatedir}/lib/%{name}

%changelog
%autochangelog
