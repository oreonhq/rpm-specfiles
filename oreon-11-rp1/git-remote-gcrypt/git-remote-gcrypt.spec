%global source0_hash 0a0b8359eccdd5d63eaa3b06b7a24aea813d7f1e8bf99536bdd60bc7f18dca03

Name:       git-remote-gcrypt
Version:    1.5
Release:    10%{?dist}
Summary:    GNU Privacy Guard-encrypted git remote

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:    GPL-3.0-only
URL:        https://git.spwhitton.name/%{name}
Source0:    https://git.spwhitton.name/%{name}/snapshot/%{name}-%{version}.tar.gz

BuildArch:  noarch

BuildRequires:  python3-docutils
Requires:   gnupg2 git-core

%description
This lets git store git repositories in encrypted form.
It supports storing repositories on rsync or sftp servers.
It can also store the encrypted git repository inside a remote git
repository. All the regular git commands like git push and git pull
can be used to operate on such an encrypted repository.

The aim is to provide confidential, authenticated git storage and
collaboration using typical untrusted file hosts or services.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}

%build
:

%install
export DESTDIR="%{buildroot}"
export prefix="%{_prefix}"
./install.sh

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%license COPYING
%doc CHANGELOG CONTRIBUTING.rst README.rst

%changelog
%autochangelog
