%global source2_hash 3e9059cae331058f2e7bbfbbad7944431536b269083976d0842b95d65c9efa1f
%global source1_hash 2f7c360eddab5ff9a9b8ee91d45541f00a86289984075de260b12e3f8476262f
%global source0_hash c15fbfce24a2bf316b5ae795d891f84e7e5ddb583ba2886a55387f40ae767041
Name:           dd_rescue
Version:        1.99.22
Release:        1%{?dist}
Summary:        Fault tolerant "dd" utility for rescuing data from bad media
License:        GPL-2.0-only OR GPL-3.0-only
URL:            http://www.garloff.de/kurt/linux/ddrescue/
%global         rhelp_version 0.3.0
Source0:        http://www.garloff.de/kurt/linux/ddrescue/dd_rescue-%{version}.tar.bz2
Source1:        http://www.kalysto.org/pkg/dd_rhelp-%{rhelp_version}.tar.gz
Source2:        http://www.garloff.de/kurt/linux/ddrescue/dd_rescue-%{version}.tar.bz2.asc
Source3:        gpgkey-6669F7340D31E95EC5565490DE4F1B3A2BFFC5BF.gpg
Patch0:         dd_rescue-rhelp_version.patch
Requires:       grep
Requires:       sed
Requires:       coreutils
Requires:       bc
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bc
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  grep
BuildRequires:  lzo-devel
BuildRequires:  make
BuildRequires:  xz-devel
# /oreon:deps
%description
The dd_rescue is a utility similar to the system utility "dd" which copies
data from a file or block device to another. The dd_rescue does however
not abort on errors in the input file. This makes it suitable for
rescuing data from media with errors, e.g. a disk with bad sectors.

This package includes dd_rhelp wrapper script facilitating data
recovery. It is trying to make it so simple to recover as:
dd_rhelp source target

Please note Fedora ships also GNU ddrescue, which probably gives
faster and more reliable results rescuing whole disks.
But still there might be some niche pattern of bad sectors,
which might get better covered by dd_rescue and both tools
might be used with sub-sequent runs cooperatively on the same disk image.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gpgv2 --keyring %{SOURCE3} %{SOURCE2} %{SOURCE0}
%setup -q -n %{name}-%{version}
%setup -q -n %{name}-%{version} -a 1 -D -T
%autopatch -p 1

%build

autoreconf -vif
%configure
%ifarch ppc64le
rm -f aesni.c find_nonzero_sse2.c find_nonzero_arm.c find_nonzero_arm64.c
%endif
make RPM_OPT_FLAGS="%{optflags}" %{?_smp_mflags} LIB=%{_lib}
cp -p README.dd_rescue README
cp -p dd_rhelp-%{rhelp_version}/README README.dd_rhelp
cp -p dd_rhelp-%{rhelp_version}/FAQ FAQ.dd_rhelp
%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALLDIR=%{buildroot}/%{_bindir} INSTASROOT="" INSTALLFLAGS="" LIB=%{_lib}
install -D -m 755 dd_rhelp-%{rhelp_version}/dd_rhelp %{buildroot}%{_bindir}/dd_rhelp
%oreon_autofiles main

%check

pushd dd_rhelp-%{rhelp_version}
PATH="../:$PATH" bash ./dd_rhelp.test &&
popd
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
