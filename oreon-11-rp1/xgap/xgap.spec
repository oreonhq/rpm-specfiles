%global source0_hash 5330f59825c662670cb5e40f6500c76c318760c7dd403cfb40ed8772ed93a3ff
%global gap_pkgname xgap
%global giturl      https://github.com/gap-packages/xgap
Name:           %{gap_pkgname}
Version:        4.33
Release:        1%{?dist}
Summary:        GUI for GAP
License:        GPL-2.0-or-later AND HPND
URL:            https://gap-packages.github.io/xgap/
VCS :           git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        XGap
Patch:          %{name}-warning.patch
Patch:          %{name}-incompatible-pointer.patch
Patch:          %{name}-gap-path.patch
ExcludeArch:    %{ix86}
BuildSystem:    gap
BuildOption(install): bin examples htm lib tst
BuildOption(check): tst/testall.g
Requires:       gap%{?_isa}
Provides:       gap-pkg-%{gap_pkgname} = %{version}-%{release}
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-smallgrp-doc
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  tth
# /oreon:deps
%description
An X Windows GUI for GAP.

%package doc
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only
Summary:        XGap documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-pkg-smallgrp-doc
%description doc
This package contains documentation for %{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0

%build

export CFLAGS='%{build_cflags} -D_GNU_SOURCE'
%configure --with-gaproot=%{gap_archdir}
%make_build
sed -i "s,$PWD,\$GAP_DIR/pkg/%{name}-%{version}," bin/xgap.sh
ln -s %{gap_libdir}/etc ../../etc
ln -s %{gap_libdir}/doc ../../doc
ln -s %{gap_libdir}/pkg/smallgrp ..
ln -s %{name}-%{version} ../%{name}
cd doc
./make_doc
cd -
rm -f ../%{name} ../smallgrp ../../{doc,etc}
%install -a
mkdir -p %{buildroot}%{_bindir}
mv %{buildroot}%{gap_archdir}/pkg/%{name}/bin/xgap.sh %{buildroot}%{_bindir}/xgap
rm %{buildroot}%{gap_archdir}/pkg/%{name}/bin/*/{Makefile,config*,*.o}
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --mode=644 --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE1}
mkdir -p %{buildroot}%{_datadir}/X11/app-defaults
cp -p %{SOURCE2} %{buildroot}%{_datadir}/X11/app-defaults
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check -p

sed -i.orig 's|"-p"|"-l","%{buildroot}%{gap_archdir};",&|' \
   %{buildroot}%{gap_archdir}/pkg/%{name}/tst/xgap_test.g
%check -a

mv %{buildroot}%{gap_archdir}/pkg/%{name}/tst/xgap_test.g.orig \
   %{buildroot}%{gap_archdir}/pkg/%{name}/tst/xgap_test.g
%files -f %{oreon_filedir}/main.list
%files -n xgap-doc -f %{oreon_filedir}/xgap-doc.list

%changelog

%autochangelog
