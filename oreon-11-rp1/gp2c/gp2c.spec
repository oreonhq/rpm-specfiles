%global source0_hash 245ce020fd7862dc2889f866ceef1523a4953f19bf1e5dc3db44988b5e0726bc
%bcond autoreconf 1
%global upver 0.0.14pl1
Name:           gp2c
Version:        %{gsub %{upver} pl .}
Release:        1%{?dist}
Summary:        PARI/GP script to C program translator
License:        GPL-2.0-or-later AND GPL-3.0-or-later WITH Bison-exception-2.2
SourceLicense:  %{license} AND FSFUL AND FSFULLR AND X11
URL:            https://pari.math.u-bordeaux.fr/
VCS:            git:https://pari.math.u-bordeaux.fr/git/gp2c.git
Source0:        https://pari.math.u-bordeaux.fr/pub/pari/GP2C/%{name}-%{upver}.tar.gz
Source1:        %{url}pub/pari/GP2C/gp2c-%{upver}.tar.gz.asc
Source2:        gpgkey-42028EA404A2E9D80AC453148F0E7C2B4522E387.gpg
ExcludeArch:    %{ix86}
%if %{with autoreconf}
%endif
Requires:       gcc
Requires:       pari-devel%{?_isa}
Recommends:     pari-gp
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gpgverify
BuildRequires:  make
BuildRequires:  pari-devel
BuildRequires:  pari-gp
BuildRequires:  perl
BuildRequires:  tex(latex)
# /oreon:deps
%description
GP2C is a PARI/GP script to C program translator.

%package        doc
Summary:        Documentation for gp2c
BuildArch:      noarch
%description    doc
This package contains documentation for GP2C.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --data=%{SOURCE0} --signature=%{SOURCE1} --keyring=%{SOURCE2}
%autosetup -n gp2c-%{upver}

# Convert to Unicode
iconv -f ISO8859-1 -t UTF-8 ChangeLog > ChangeLog.utf8
touch -r ChangeLog ChangeLog.utf8
mv ChangeLog.utf8 ChangeLog

# Regenerate the documentation
rm -v doc/*.{dvi,html,pdf}

%conf
%if %{with autoreconf}
autoreconf --force --install --verbose
%endif
%configure --with-paricfg='%{_libdir}/pari/pari.cfg'

%build

%make_build
cd doc
pdflatex -interaction=nonstopmode gp2c.tex
pdflatex -interaction=nonstopmode gp2c.tex
pdflatex -interaction=nonstopmode gp2c.tex
pdflatex -interaction=nonstopmode type.tex
pdflatex -interaction=nonstopmode type.tex
cd -
%install
%make_install
rm -vrf '%{buildroot}%{_docdir}/gp2c'
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%make_build check
%files -f %{oreon_filedir}/main.list
%files -n gp2c-doc -f %{oreon_filedir}/gp2c-doc.list

%changelog

%autochangelog
