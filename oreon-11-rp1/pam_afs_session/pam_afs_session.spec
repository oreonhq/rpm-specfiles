%global source0_hash bf6c2a60a079ec53917d268a97d030735e6189fb56900d35c6f6b0191b5dfcc5

Name: pam_afs_session
Summary: AFS PAG and AFS tokens on login
Version: 2.6
Release: 25%{?dist}
License: MIT
URL: https://www.eyrie.org/~eagle/software/pam-afs-session/
Source: https://archives.eyrie.org/software/afs/pam-afs-session-%{version}.tar.gz
BuildRequires: make
BuildRequires:  gcc
BuildRequires: pam-devel
BuildRequires: krb5-devel
%description
pam-afs-session is a PAM module intended for use with a Kerberos v5 PAM module
to obtain an AFS PAG (Process Authentication Group) and AFS tokens on login. It
puts every new session in a PAG regardless of whether it was authenticated with
Kerberos and runs a configurable external program to obtain tokens.

%define pamdir /%{_lib}/security

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pam-afs-session-%{version}
# remove non-redhat examples
find examples -mindepth 1 -maxdepth 1 -not -name "redhat" -exec rm -rf {} ';'

%build
%configure --libdir=/%{_lib} --with-aklog=%{_bindir}/aklog
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{pamdir}/*.la

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc NEWS README TODO examples
%{pamdir}/pam_afs_session.so
%{_mandir}/man5/pam_afs_session.5.gz

%changelog
%autochangelog
