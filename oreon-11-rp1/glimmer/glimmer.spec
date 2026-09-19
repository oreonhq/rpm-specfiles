%global source0_hash a531f83b6162064539bebedbef5bec6b99df32b5d2877ba4431d2fa93faa78a3

Name:           glimmer
Version:        3.02b
Release:        31%{?dist}
Summary:        System for finding genes in microbial DNA

# Automatically converted from old format: Artistic clarified - review is highly recommended.
License:        ClArtistic
URL:            http://www.cbcb.umd.edu/software/glimmer
Source0:        http://www.cbcb.umd.edu/software/glimmer/glimmer302b.tar.gz
BuildRequires:  gcc-c++
BuildRequires: make
Requires:       elph

%description
Glimmer is a system for finding genes in microbial DNA, especially the genomes
of bacteria, archaea, and viruses. Glimmer (Gene Locator and Interpolated
Markov ModelER) uses interpolated Markov models (IMMs) to identify the coding
regions and distinguish them from noncoding DNA.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n glimmer3.02
rm -f sample-run/g3-*
sed -i "s+/fs/szgenefinding/Glimmer3/bin+%{_libexecdir}/glimmer3+" scripts/g3-*
sed -i "s+/fs/szgenefinding/Glimmer3/scripts+%{_datadir}/glimmer3+" scripts/g3-*
sed -i "s+/nfshomes/adelcher/bin/elph+%{_bindir}/elph+" scripts/g3-*
sed -i "s/@ if/if/" src/c_make.gen

%build
make -C src %{?_smp_mflags} CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"

%check

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}/glimmer3
mkdir -p $RPM_BUILD_ROOT%{_datadir}/glimmer3
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 scripts/g3-* $RPM_BUILD_ROOT/%{_bindir}
install -m 755 bin/[a-su-z]* $RPM_BUILD_ROOT%{_libexecdir}/glimmer3
install -m 755 scripts/*.awk $RPM_BUILD_ROOT%{_datadir}/glimmer3
ln -s ../libexec/glimmer3/glimmer3 $RPM_BUILD_ROOT/%{_bindir}/glimmer3

%files
%doc LICENSE glim302notes.pdf sample-run
%{_bindir}/*
%{_datadir}/glimmer3/
%{_libexecdir}/glimmer3/

%changelog
%autochangelog
