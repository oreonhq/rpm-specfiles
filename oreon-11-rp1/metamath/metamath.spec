%global source0_hash 0fe8255ac5af338670845e1e496905f8253b6cdaa62b5efb663f4de31232799b

Name:           metamath
Version:        0.198
Release:        11%{?dist}
Summary:        Construct mathematics from basic axioms

License:        GPL-2.0-or-later
URL:            https://us.metamath.org/
VCS:            site:https://github.com/metamath/metamath-exe.git
Source0:        https://us.metamath.org/downloads/%{name}.tar.bz2
Source1:        https://us.metamath.org/latex/%{name}.tex

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  tex(latex)
BuildRequires:  tex(makecell.sty)
BuildRequires:  tex(needspace.sty)
BuildRequires:  tex(tabu.sty)

Suggests:       rlwrap

%description
Metamath is a tiny language that can express theorems in abstract mathematics,
accompanied by proofs that can be verified by a computer program.  Metamath
lets you see mathematics developed in complete detail from first principles,
with absolute rigor.

%package        theories
Summary:        Existing mathematical theories in the metamath format
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

# peano.mm is GPL-2.0-or-later; all other theory files are CC0
License:        GPL-2.0-or-later AND CC0-1.0

%description    theories
This package contains metamath theory files for several branches of
mathematics, such as ZFC set theory, HOL, and Peano arithmetic.

%package        doc
# The content is CC0-1.0.  The remaining licenses cover the various fonts
# embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
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

# Build the manual
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

# Install all of the theories
cp -p *.mm %{buildroot}%{_datadir}/metamath

# Install the manual
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -p %{name}.pdf %{buildroot}%{_docdir}/%{name}

%check
# Check proof validity
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

%files
%doc README.TXT
%license LICENSE.TXT
%{_bindir}/metamath
%{_mandir}/man1/metamath.1*

%files theories
%{_datadir}/metamath/

%files doc
%license LICENSE.TXT
%dir %{_docdir}/metamath/
%{_docdir}/metamath/metamath.pdf

%changelog
%autochangelog
