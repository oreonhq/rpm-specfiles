%global source0_hash 367c52b99c0b0a4794b215181439bf54abe4998872d3ef25d793bc13c4d40e42
Name:           cohomCalg
Version:        0.32
Release:        1%{?dist}
Summary:        Sheaf cohomologies for line bundles on toric varieties
License:        GPL-3.0-or-later
URL:            https://github.com/BenjaminJurke/cohomCalg
VCS:            git:%{url}.git
Source0:        https://github.com/BenjaminJurke/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}-test.tar.xz
Patch:          https://github.com/BenjaminJurke/cohomCalg/commit/e2c2635.patch
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  tex(extdash.sty)
BuildRequires:  tex(hyperxmp.sty)
BuildRequires:  tex(latex)
BuildRequires:  tex(totpages.sty)
BuildRequires:  texlive-rsfs
BuildRequires:  texlive-txfonts
BuildRequires:  texlive-utopia
# /oreon:deps
%description
This package computes sheaf cohomologies for line bundles on toric varieties.

%package doc
License:        GPL-3.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND LicenseRef-Utopia
Summary:        Manual for %{name}
BuildArch:      noarch
%description doc
User manual for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -a 1

%conf
# Remove prebuilt Windows binaries and the prebuilt manual
rm -f bin/*.exe manual.pdf

%build

%make_build CFLAGS="%{build_cflags}" CXXFLAGS="%{build_cxxflags}"
cd manual/latex_source
pdflatex manual
bibtex manual
pdflatex manual
pdflatex manual
%install
mkdir -p %{buildroot}%{_bindir}
cp -p bin/cohomcalg %{buildroot}%{_bindir}
%oreon_autofiles cohomCalg-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd bin
for fil in CP2 P31SU7 Quintic WCP11114 dP1 dP3; do
  ./cohomcalg --integrated $fil.in 2>/dev/null | diff -q out/$fil.out -
done
popd
%files -f %{oreon_filedir}/main.list
%files -n cohomCalg-doc -f %{oreon_filedir}/cohomCalg-doc.list

%changelog

%autochangelog
