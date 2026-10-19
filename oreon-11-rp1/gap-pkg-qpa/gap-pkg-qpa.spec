%global source0_hash 71748de693f4a8d979bac42083866e85edf12462bfddce187e6481729338c27e
%global gap_pkgname qpa
%global giturl      https://github.com/gap-packages/qpa
Name:           gap-pkg-%{gap_pkgname}
Version:        1.37
Release:        1%{?dist}
Summary:        GAP package for quivers and path algebras
License:        GPL-2.0-or-later
URL:            https://folk.ntnu.no/oyvinso/QPA/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/%{gap_pkgname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    gap
BuildOption(build): --packagedirs ..
BuildOption(install): examples lib tst version
BuildOption(check): tst/testall.g
Requires:       gap-pkg-gbnp
# oreon:deps
BuildRequires:  GAPDoc-latex
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-gbnp
BuildRequires:  tex(beamer.cls)
BuildRequires:  tex(pcrr8t.tfm)
BuildRequires:  tex(textpos.sty)
BuildRequires:  tex(xy.sty)
# /oreon:deps
%description
This package carries out computations for finite dimensional quotients of path
algebras over the fields that are available in GAP.  QPA stands for "Quivers
 and Path Algebras".

%package doc
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only AND LicenseRef-Rsfs
Summary:        QPA documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%conf
# Fix a broken reference
sed -i 's/Basic Construction/Constructing Quivers/' doc/chapter_path_algebras.xml

%build -a

cd doc/gap-days-lectures
pdflatex lecture1
pdflatex lecture1
pdflatex lecture2
pdflatex lecture2
pdflatex lecture3
pdflatex lecture3
pdflatex lecture4a
pdflatex lecture4a
%install -a
%gap_copy_docs -d doc/gap-days-lectures
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-qpa-doc -f %{oreon_filedir}/gap-pkg-qpa-doc.list

%changelog

%autochangelog
