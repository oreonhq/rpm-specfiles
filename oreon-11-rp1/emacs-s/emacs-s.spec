%global source0_hash a29b75866a423954c8b003d9f0d760a3153938336873843d9b0ec223e0243f3f

%global pkg s

Name:           emacs-%{pkg}
Version:        1.13.0
Release:        10%{?dist}
Summary:        The long lost Emacs string manipulation library

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/magnars/%{pkg}.el/
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  emacs
Requires:       emacs(bin) >= %{_emacs_version}
BuildArch:      noarch

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pkg}.el-%{version}

%build
%{_emacs_bytecompile} %{pkg}.el

%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 %{pkg}.el* -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/

%check
./run-tests.sh

%files
%doc README.md
%license LICENSE
%{_emacs_sitelispdir}/%{pkg}/

%changelog
%autochangelog
