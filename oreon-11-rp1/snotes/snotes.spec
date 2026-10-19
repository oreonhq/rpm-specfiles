%global source0_hash 7a8ded378efebe07b691197b42fe6ab6ce4193ffffdea477d6c6d618f9f3f386
Name:           snotes
Version:        1.1
Release:        1%{?dist}
Summary:        A flexible and easy to use notes system
License:        MIT
URL:            https://github.com/v4hn/%{name}
Source0:        https://github.com/v4hn/%{name}/archive/v%{version}.tar.gz
BuildArch:      noarch
Requires:       dmenu
Requires:       git
Requires:       vim-minimal
Requires:       xterm
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

make
%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
