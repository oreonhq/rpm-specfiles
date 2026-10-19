%global source0_hash f17ab26a87af639876989ddcd31b0b0d73f812a5cbab920b5566571122389626
%global gap_pkgname smallclassnr
%global gap_upname  SmallClassNr
%global giturl      https://github.com/stertooy/SmallClassNr
Name:           gap-pkg-%{gap_pkgname}
Version:        1.7.2
Release:        1%{?dist}
Summary:        Library of finite groups with small class number
License:        GPL-2.0-or-later
URL:            https://stertooy.github.io/SmallClassNr/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/%{gap_upname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    gap
BuildOption(build): --packagedirs ..
BuildOption(install): data lib tst
BuildOption(check): tst/testall.g
Requires:       gap-core
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-packagemanager-doc
# /oreon:deps
%description
The SmallClassNr package provides access to finite groups with small class
number.  Currently, the package contains the finite groups of class number at
most 14.

%package doc
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        SmallClassNr documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
Recommends:     gap-pkg-packagemanager-doc
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-smallclassnr-doc -f %{oreon_filedir}/gap-pkg-smallclassnr-doc.list

%changelog

%autochangelog
