%global source1_hash bfc66576d9d037fd436472744a2dfc81dc2880b70bacb4934ed6f9381f031284
%global source0_hash 1a8eace82d704e8a35e4d43c88ce2892dde483714a630f58210eb21b7c3b9276
Name:           metamath
Version:        0.198
Release:        1%{?dist}
Summary:        Construct mathematics from basic axioms
License:        GPL-2.0-or-later
URL:            https://us.metamath.org/
VCS:            site:https://github.com/metamath/metamath-exe.git
Source0:        https://us.metamath.org/downloads/%{name}.tar.bz2
Source1:        https://us.metamath.org/latex/%{name}.tex
ExcludeArch:    %{ix86}
Suggests:       rlwrap
# oreon:deps
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  tex(latex)
BuildRequires:  tex(makecell.sty)
BuildRequires:  tex(needspace.sty)
BuildRequires:  tex(tabu.sty)
# /oreon:deps
%description
Metamath is a tiny language that can express theorems in abstract mathematics,
accompanied by proofs that can be verified by a computer program.  Metamath
lets you see mathematics developed in complete detail from first principles,
with absolute rigor.

%package        theories
Summary:        Existing mathematical theories in the metamath format
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
License:        GPL-2.0-or-later AND CC0-1.0
%description    theories
This package contains metamath theory files for several branches of
mathematics, such as ZFC set theory, HOL, and Peano arithmetic.

%package        doc
License:        CC0-1.0 AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later
Summary:        The Metamath book
BuildArch:      noarch
%description    doc
This package contains The Metamath book, which provides an in-depth
understanding of the Metamath language and program.  The first part of the
book also includes an easy-to-read informal discussion of abstract mathematics
and computers, with references to other proof verifiers and automated theorem
provers.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}

%conf
cp -p %{SOURCE1} .
touch special-settings.sty

# Remove prebuilt objects
rm metamath.exe

# Do not override our choice of CFLAGS
sed -i '/Try to optimize/,/^$/d' configure.ac

# Generate the configure script
autoreconf -fi

%build

%configure CFLAGS="%{build_cflags} -DINLINE=inline -fwrapv"
%make_build
touch metamath.ind
pdflatex metamath
pdflatex metamath
bibtex metamath
makeindex metamath.idx
pdflatex metamath
pdflatex metamath
pdflatex metamath
%install
%make_install
cp -p *.mm %{buildroot}%{_datadir}/metamath
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -p %{name}.pdf %{buildroot}%{_docdir}/%{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

run_verify() {
./metamath << EOF
read $1
set scroll continuous
verify proof *
quit
EOF
}
for fil in *.mm; do
  run_verify $fil
done
%files -f %{oreon_filedir}/main.list
%files -n metamath-theories -f %{oreon_filedir}/metamath-theories.list
%files -n metamath-doc -f %{oreon_filedir}/metamath-doc.list

%changelog

%autochangelog
