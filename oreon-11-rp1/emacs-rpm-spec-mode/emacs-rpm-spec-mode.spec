%global source0_hash d97105ac69850fa1e1e988ed3043ee42618443de6715609d9f48178fe54634ae
%global commit  283d2aac4ede343586a1fb9e9d2a5917f34809a1
%global date    20241209
%global forgeurl https://github.com/Thaodan/rpm-spec-mode
Name:           emacs-rpm-spec-mode
Version:        0.16
Release:        1%{?dist}
Summary:        Major GNU Emacs mode for editing RPM spec files
%forgemeta
License:        GPL-2.0-or-later
URL:            https://github.com/Thaodan/rpm-spec-mode
VCS:            git:%{url}.git
Source0:        %{forgeurl}/archive/%{commit}/rpm-spec-mode-%{commit}.tar.gz
BuildArch:      noarch
Requires:       emacs(bin) >= %{?_emacs_version}%{!?_emacs_version:0}
# oreon:deps
BuildRequires:  emacs-nw
# /oreon:deps
%description
Major GNU Emacs mode for editing RPM spec files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build

%_emacs_bytecompile rpm-spec-mode*.el
emacs -batch --no-init-file --no-site-file \
  --eval "(let ((backup-inhibited t)) (loaddefs-generate \".\" \"$PWD/rpm-spec-mode-loaddefs.el\"))"
%install
mkdir -p %{buildroot}/%{_emacs_sitelispdir}
install -p -m 644 rpm-spec-mode.el{,c} %{buildroot}/%{_emacs_sitelispdir}
mkdir -p %{buildroot}%{_emacs_sitestartdir}
install -p -m 644 rpm-spec-mode-loaddefs.el %{buildroot}%{_emacs_sitestartdir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
