%global source0_hash 68d1a0f62fc40b7d7a212a277005f2f4bb805c49c26a7674daf10b357b23f933

%global date    20240427
%global commit  effa1dcce85c878236f8313133dff1a2b766cd7c
%global forgeurl https://github.com/marijnheule/drat-trim

Name:           drat-trim
Version:        0
Summary:        Proof checker for DIMACS proofs

%forgemeta

Release:        0.30%{?dist}
License:        MIT
URL:            %{forgeurl}
VCS:            git:%{forgeurl}.git
Source:         %{forgesource}
# Drat2er wants to use drat-trim as a library, but drat-trim only provides a
# binary.  Modify the sources to provide a library.
Patch:          %{name}-library.patch
# Drat2er and CVC5 do not want to see commentary.  Apply a patch from the
# drat2er developers to optionally make it shut up.
Patch:          %{name}-silent.patch
# Eliminate maybe-uninitialized warnings
Patch:          %{name}-uninit.patch
# Work around an integer overflow that leads to a segfault
# https://github.com/marijnheule/drat-trim/pull/36
Patch:          %{name}-overflow.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc
BuildRequires:  help2man

%description
The proof checker DRAT-trim can be used to check whether a propositional
formula in the DIMACS format is unsatisfiable.  Given a propositional formula
and a clausal proof, DRAT-trim validates that the proof is a certificate of
unsatisfiability of the formula.  Clausal proofs should be in the DRAT format
which is used to validate the results of the SAT competitions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers files and library links for developing applications that use
%{name}.

%package        tools
Summary:        Command line interface to %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tools
This package contains a command line interface to %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build
CFLAGS='%{build_cflags} -DLONGTYPE %{build_ldflags}'

# Build the library
gcc $CFLAGS -fPIC -shared -Wl,-h,lib%{name}.so.0 -o lib%{name}.so.0.0.0 \
  %{name}.c
ln -s lib%{name}.so.0.0.0 lib%{name}.so.0
ln -s lib%{name}.so.0 lib%{name}.so

# Build the command line interface
gcc $CFLAGS -o %{name} %{name}-main.c -L. -l%{name}
export LD_LIBRARY_PATH=$PWD

# Build the other tools
gcc $CFLAGS -o lrat-check lrat-check.c
gcc $CFLAGS -o drat-compress compress.c
gcc $CFLAGS -o drat-decompress decompress.c
gcc $CFLAGS -o drat-gapless gapless.c

# Make man page for the command line interface
help2man --version-string=%{date} -N -o %{name}.1 \
  -n 'Proof checker for DIMACS proofs' ./%{name}

%install
# Install the library
mkdir -p %{buildroot}%{_libdir}
cp -a lib%{name}.so* %{buildroot}%{_libdir}

# Install the header file
mkdir -p %{buildroot}%{_includedir}
cp -p %{name}.h %{buildroot}%{_includedir}

# Install the binaries
mkdir -p %{buildroot}%{_bindir}
cp -p drat-compress drat-decompress drat-gapless drat-trim lrat-check \
   %{buildroot}%{_bindir}

# Install the man page
mkdir -p %{buildroot}%{_mandir}/man1
cp -p drat-trim.1 %{buildroot}%{_mandir}/man1

%check
# Do not rebuild the binaries without Fedora flags
sed -i '/make/d' run-examples

export LD_LIBRARY_PATH=$PWD
sh ./run-examples

%files
%license LICENSE
%{_libdir}/lib%{name}.so.0{,.*}

%files          devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so

%files          tools
%doc README.md
%{_bindir}/drat-compress
%{_bindir}/drat-decompress
%{_bindir}/drat-gapless
%{_bindir}/drat-trim
%{_bindir}/lrat-check
%{_mandir}/man1/drat-trim.1*

%changelog
%autochangelog
