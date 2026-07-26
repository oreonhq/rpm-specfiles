%global source0_hash 782547cc4db6591d9db015eac49062e62837b2bd4bc4bdaa358a60e268081242

Name:           snotes
Version:        1.0
Release:        26%{?dist}
Summary:        A flexible and easy to use notes system
License:        MIT
URL:            https://github.com/v4hn/%{name}
Source0:        https://github.com/v4hn/%{name}/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
Requires:       dmenu
Requires:       git
# The default editor
Requires:       vim-minimal
Requires:       xterm

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
# Let's have a cookie!
make

%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix}

%files
%license LICENSE
%doc README
%{_bindir}/snotes*

%changelog
%autochangelog
