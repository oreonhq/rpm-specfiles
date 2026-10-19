%global source0_hash 9bc4806146e5b9dcf574df034f8b392f746444eeca012ba9c4a67599be7800e3
%global pkg ansible
Name:           emacs-%{pkg}
Version:        0.4.3
Release:        1%{?dist}
Summary:        Ansible minor mode
License:        GPL-2.0-or-later
URL:            https://gitlab.com/%{name}/%{name}
Source0:        https://gitlab.com/%{name}/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{pkg}-init.el
Requires:       emacs(bin) >= %{_emacs_version}
Requires:       emacs-f
Requires:       emacs-s
BuildArch:      noarch
# oreon:deps
BuildRequires:  emacs
BuildRequires:  emacs-f
BuildRequires:  emacs-s
# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%{_emacs_bytecompile} %{pkg}.el
%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 %{pkg}.el* -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
cp -a dict/ snippets/ $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -Dpm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_emacs_sitestartdir}/%{pkg}-init.el
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
