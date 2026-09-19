%global source0_hash 1625c5b34528ddd84fb8681ca2679eab22f3c9ade6a02f825b2fdbd4e1942736

Name:           pam_2fa
Version:        1.0
Release:        19%{?dist}
Summary:        Second factor authentication for PAM

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://cern-cert.github.io/pam_2fa/
Source0:        https://github.com/CERN-CERT/pam_2fa/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  pam-devel
BuildRequires:  curl-devel
BuildRequires:  openldap-devel
BuildRequires:  ykclient-devel
BuildRequires:  automake
BuildRequires:  libtool
Requires:       pam

%description
The PAM 2FA module provides a second factor authentication, which can be
combined with the standard PAM-based password authentication to ask for:

 *  What you know: user account password ( standard PAM modules )
 *  What you have (pick one of): (PAM 2FA)

 *  A Google Authenticator Application on your phone
 *  A Phone Number capable of receiving SMS
 *  A Yubikey

%package -n pam_ssh_user_auth
Summary:        PAM module to help with %{!?el7:SSH_AUTH_INFO_0}%{?el7:SSH_USER_AUTH}
Requires:       pam

%description -n pam_ssh_user_auth
pam_ssh_user_auth checks the value of %{!?el7:SSH_AUTH_INFO_0}%{?el7:SSH_USER_AUTH} and will return success
if is non-empty and failure if it is.  It can be used to skip other PAM
authentication methods with a configuration like:

auth       [success=1 ignore=ignore default=die] pam_ssh_user_auth.so
auth       substack     password-auth

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%{!?el7:sed -i -e s/SSH_USER_AUTH/SSH_AUTH_INFO_0/ *.c}

%build
autoreconf -i
%configure --libdir=/%{_lib} \
           --with-pam-dir=/%{_lib}/security/
%make_build

%install
%make_install

%files
%license COPYING
%doc README.md
/%{_lib}/security/pam_2fa.so

%files -n pam_ssh_user_auth
%license COPYING
%doc README.md
/%{_lib}/security/pam_ssh_user_auth.so

%changelog
%autochangelog
