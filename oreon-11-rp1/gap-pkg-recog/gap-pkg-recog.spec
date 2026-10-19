%global source0_hash 2cae443c6f7dfb738e4470fcce526dba1ee3155dc26c27818694023255c77064
%global gap_pkgname recog
%global giturl      https://github.com/gap-packages/recog
Name:           gap-pkg-%{gap_pkgname}
Version:        1.5.1
Release:        1%{?dist}
Summary:        Group recognition methods
License:        GPL-3.0-or-later
URL:            https://gap-packages.github.io/recog/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_pkgname}-%{version}.tar.bz2
Source1:        %{name}-testdata.tar.xz
BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): contrib examples gap tst
Requires:       gap-pkg-atlasrep
Requires:       gap-pkg-factint
Requires:       gap-pkg-forms
Requires:       gap-pkg-genss
Requires:       gap-pkg-orb
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-atlasrep
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-ctbllib
BuildRequires:  gap-pkg-factint
BuildRequires:  gap-pkg-forms
BuildRequires:  gap-pkg-genss
BuildRequires:  gap-pkg-orb
BuildRequires:  gap-pkg-tomlib
# /oreon:deps
%description
This is a GAP package for group recognition.

%package doc
License:        GPL-3.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Recog documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version} -b 1

%check

mkdir ~/.gap
cat > ~/.gap/gap.ini << EOF
SetUserPreference( "AtlasRep", "AtlasRepDataDirectory", "%{_builddir}/atlasrep/" );
EOF
gap -l '%{buildroot}%{gap_libdir};' tst/testquick.g
gap -l '%{buildroot}%{gap_libdir};' tst/testslow.g
%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-recog-doc -f %{oreon_filedir}/gap-pkg-recog-doc.list

%changelog

%autochangelog
