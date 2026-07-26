%global source0_hash 1cba04a59c8109389079b479c1bf5719b595e799680e10d35ce9aa091cb752af

Name:           git-secret
Version:        0.5.0
Release:        10%{?dist}
Summary:        A bash-tool to store your private data inside a git repository

License:        MIT
URL:            http://git-secret.io/
Source0:        https://github.com/sobolevn/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
Requires:       bash        >= 3.2.57
Requires:       gawk        >= 4.0.2
Requires:       git         >= 1.8.3.1
Requires:       gpg         >= 1.4
# sha256sum is needed, provided in coreutils

%description
git-secret is a bash tool which stores private data inside a git repository.
It encrypts tracked files with public keys for users whom you trust using GPG,
allowing permitted users to access encrypted data using their secret keys.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%make_build

%install
%make_install

%files
%license LICENSE.md
%{_bindir}/git-secret
%{_mandir}/man1/git-secret*
%{_mandir}/man7/git-secret*

%changelog
%autochangelog
