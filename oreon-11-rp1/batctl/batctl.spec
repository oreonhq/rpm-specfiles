%global source100_hash 729cf9654634d22ee218720f76499822f1df54e18dcf4a1de8b296415557c762
%global source1_hash 1ec04fe3b075bcda02a8f59958be82dc36eb5ee782eefb3f398934131d6e85ba
%global source0_hash 2c8443fae7b3471a500837f8cfbbc2b7bbab602e43ce8c61b100560dec1d9ee0
Name:           batctl
Version:        2026.3
Release:        1%{?dist}
Summary:        B.A.T.M.A.N. advanced control and management tool
License:        GPL-2.0-only AND MIT AND ISC
URL:            http://www.open-mesh.org/
Source0:        http://downloads.open-mesh.org/batman/stable/sources/batctl/%{name}-%{version}.tar.gz
Source1:        http://downloads.open-mesh.org/batman/stable/sources/batctl/%{name}-%{version}.tar.gz.asc
Source100:      https://keys.openpgp.org/pks/lookup?op=get&options=mr&search=0x2DE9541A85CC87D5D9836D5E0C8A47A2ABD72DF9#/sw.asc
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libnl3-devel
BuildRequires:  make
# /oreon:deps
%description
batctl offers a convenient way to configure the batman-adv kernel module
as well as displaying debug information such as originator tables,
translation tables and the debug log. In combination with a bat-hosts
file batctl allows the use of host names instead of MAC addresses.

B.A.T.M.A.N. advanced operates on layer 2. Thus all hosts participating
in the virtual switched network are transparently connected together
for all protocols above layer 2. Therefore the common diagnosis tools
do not work as expected. To overcome these problems batctl contains the
commands ping, traceroute, tcpdump which provide similar functionality
to the normal ping(1), traceroute(1), tcpdump(1) commands, but modified
to layer 2 behavior or using the B.A.T.M.A.N. advanced protocol.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

cat %{S:100} > %{_builddir}/%{name}.gpg
%{gpgverify} --keyring="%{_builddir}/%{name}.gpg" --signature="%{SOURCE1}" --data="%{SOURCE0}"
%setup -q

%build

make %{?_smp_mflags} CFLAGS="%{optflags} -I%{_prefix}/include/libnl3" V=s
%install
%make_install PREFIX=%{_prefix} SBINDIR=%{_sbindir} install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
