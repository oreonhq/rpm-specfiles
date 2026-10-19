%global source0_hash 0c0f6baf2bb3a7b65f09b1f52d4016739fb60e3cf513b75284c8bea363a28748
%global pkg blacken
%global commit 880cf502198753643a3e2ccd4131ee6973be2e8a
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20210406
Name:           emacs-%{pkg}
Version:        0
Release:        1%{?dist}
Summary:        Python Black for Emacs
License:        GPL-3.0-or-later
URL:            https://github.com/pythonic-emacs/%{pkg}
Source0:        https://github.com/pythonic-emacs/%{pkg}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1:        %{pkg}-init.el
Requires:       emacs(bin) >= %{_emacs_version}
Requires:       python3-black
BuildArch:      noarch
# oreon:deps
BuildRequires:  emacs
# /oreon:deps
%description
Blacken uses black to format a Python buffer. It can be called explicitly on a
certain buffer, but more conveniently, a minor-mode 'blacken-mode' is provided
that turns on automatically running black on a buffer before saving.

To automatically format all Python buffers before saving, add the function
blacken-mode to python-mode-hook:

  (add-hook 'python-mode-hook 'blacken-mode)

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pkg}-%{commit}

%build

%{_emacs_bytecompile} %{pkg}.el
%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 %{pkg}.el* -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -Dpm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_emacs_sitestartdir}/%{pkg}-init.el
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
