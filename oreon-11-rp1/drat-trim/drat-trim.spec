%global source0_hash 68d1a0f62fc40b7d7a212a277005f2f4bb805c49c26a7674daf10b357b23f933
%global date    20240427
%global commit  effa1dcce85c878236f8313133dff1a2b766cd7c
%global forgeurl https://github.com/marijnheule/drat-trim
Name:           drat-trim
Version:        05.22.2023
Summary:        Proof checker for DIMACS proofs
%forgemeta
Release:        1%{?dist}
License:        MIT
URL:            %{forgeurl}
VCS:            git:%{forgeurl}.git
Source0:        %{forgeurl}/archive/%{commit}/%{name}-%{commit}.tar.gz
Patch:          %{name}-library.patch
Patch:          %{name}-silent.patch
Patch:          %{name}-uninit.patch
Patch:          %{name}-overflow.patch
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  help2man
# /oreon:deps
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
gcc $CFLAGS -fPIC -shared -Wl,-h,lib%{name}.so.0 -o lib%{name}.so.0.0.0 \
  %{name}.c
ln -s lib%{name}.so.0.0.0 lib%{name}.so.0
ln -s lib%{name}.so.0 lib%{name}.so
gcc $CFLAGS -o %{name} %{name}-main.c -L. -l%{name}
export LD_LIBRARY_PATH=$PWD
gcc $CFLAGS -o lrat-check lrat-check.c
gcc $CFLAGS -o drat-compress compress.c
gcc $CFLAGS -o drat-decompress decompress.c
gcc $CFLAGS -o drat-gapless gapless.c
help2man --version-string=%{date} -N -o %{name}.1 \
  -n 'Proof checker for DIMACS proofs' ./%{name}
%install
mkdir -p %{buildroot}%{_libdir}
cp -a lib%{name}.so* %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}
cp -p %{name}.h %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_bindir}
cp -p drat-compress drat-decompress drat-gapless drat-trim lrat-check \
   %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
cp -p drat-trim.1 %{buildroot}%{_mandir}/man1
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

sed -i '/make/d' run-examples
export LD_LIBRARY_PATH=$PWD
sh ./run-examples
%files -f %{oreon_filedir}/main.list
%files -n drat-trim-devel -f %{oreon_filedir}/drat-trim-devel.list
%files -n drat-trim-tools -f %{oreon_filedir}/drat-trim-tools.list

%changelog

%autochangelog
