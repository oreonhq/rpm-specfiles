%global source0_hash 29ea82b26698889ebf6786a9dae1732309d7187a00bf3609cb17df69a62634cd
Name:           rakudo
Version:        2026.08
Release:        1%{?dist}
Summary:        Raku on MoarVM, JVM, and JS
License:        Artistic-2.0
URL:            https://rakudo.org/
Source0:        https://github.com/rakudo/rakudo/releases/download/%{version}/rakudo-%{version}.tar.gz
Source1:        macros.raku
Requires:       moarvm >= %{version}
Requires:       nqp >= %{version}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libffi-devel
BuildRequires:  libtommath-devel
BuildRequires:  libuv-devel
BuildRequires:  make
BuildRequires:  mimalloc-devel
BuildRequires:  moarvm-devel
BuildRequires:  nqp
BuildRequires:  perl
# /oreon:deps
%description
Rakudo is a Raku Programming Language compiler for the MoarVM, JVM and
Javascript virtual machines.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

perl Configure.pl --prefix=%{_prefix} --backends=moar
%make_build
%install
%make_install
mkdir -p %{buildroot}%{_mandir}/man1
pod2man --center="Rakudo Manual" --release="Raku" --section=1 --name=rakudo \
    docs/running.pod | gzip -c > %{buildroot}%{_mandir}/man1/rakudo.1.gz
ln -s rakudo.1.gz %{buildroot}%{_mandir}/man1/raku.1.gz
install -pDm755 tools/install-dist.raku %{buildroot}%{_bindir}/raku-install-dist
mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d
install -pDm0644 %{SOURCE1} %{buildroot}%{_rpmconfigdir}/macros.d/macros.raku
for i in %{buildroot}%{_bindir}/perl6* %{buildroot}%{_datadir}/perl6/runtime/perl6*; do
    dir=$(dirname $i)
    f=$(basename $i | sed 's/perl6/rakudo/')
    if [ -e $dir/$f ]; then
        ln -sf $f $i
    fi
done
rm -r %{buildroot}%{_datadir}/perl6/core/precomp/
rm %{buildroot}%{_datadir}/perl6/core/repo.lock
%oreon_autofiles main

%check

%ifarch %{ix86} s390x
rm t/04-nativecall/26-varargs.t
%endif
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
