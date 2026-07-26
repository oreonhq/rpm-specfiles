%global source0_hash 4422e59bb3cf62bca3c73d1fdae771b83aab686cd044f73fe14b1b9c2af1cb1b

Name:           no-more-secrets
Version:        1.0.1
Release:        12%{?dist}
Summary:        A recreation of the "decrypting text" effect from the 1992 movie Sneakers

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/bartobri/no-more-secrets
Source0:        https://github.com/bartobri/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc
%description
A tool set to recreate the famous "decrypting text" effect as seen in the 1992
movie Sneakers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%make_build CFLAGS="%{optflags}" nms

%install
%make_install prefix=%{_prefix}

# the install target installs the sneakers man page regardless if its used or
# not
rm -f %{buildroot}%{_mandir}/man6/sneakers.6*

%files
%license LICENSE
%doc README.md
%{_bindir}/nms
%{_mandir}/man6/nms.6*

%changelog
%autochangelog
