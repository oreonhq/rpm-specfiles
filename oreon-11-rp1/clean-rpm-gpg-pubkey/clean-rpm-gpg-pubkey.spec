%global source0_hash 60989a99597eb6bc4dff53e3dd5f4007f745416198e3c769b813bccb2f56b9a2

%global forgeurl https://github.com/svarshavchik/%{name}
%global commit   7fdc8c7e85eac842b179f99f3394aba0e96c2ab8
%global date     20260224
%forgemeta

Name:           clean-rpm-gpg-pubkey
Version:        0
Release:        %{autorelease}
Summary:        Remove old PGP keys from the RPM database
License:        GPL-3.0-only
URL:            %{forgeurl}
Source:         %{forgesource}

BuildArch:      noarch
BuildRequires:  perl-generators
Requires:       /usr/bin/curl
Requires:       /usr/bin/gpg2
Requires:       /usr/bin/rpm
Requires:       /usr/bin/rpmkeys
Requires:       fedora-release-common
Requires:       fedora-repos

%{?perl_default_filter}

%description
A short Perl script for Fedora that removes old PGP keys from the RPM
database. Each Fedora release uses a different PGP keys, but there's
nothing in Fedora (at this time) that automatically removes prior Fedora
releases' PGP keys.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup

%install
install -Dt %{buildroot}%{_bindir} %{name}

%files
%doc README.md
%license COPYING
%license COPYING.GPL
%{_bindir}/%{name}

%changelog
%autochangelog
