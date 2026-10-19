%global source0_hash 744bde63cc6dd0fe43fa62e94387300390a0b3073d6b2b4a2ee61862229d3197
%global pkg terraform-mode
Name:           emacs-%{pkg}
Version:        1.1.0
Release:        1%{?dist}
Summary:        Major mode of Terraform configuration file
License:        GPL-3.0-or-later
URL:            https://github.com/syohex/%{name}
Source0:        https://github.com/syohex/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{pkg}-init.el
Requires:       emacs(bin) >= %{_emacs_version}
Requires:       emacs-hcl-mode
BuildArch:      noarch
# oreon:deps
BuildRequires:  emacs
BuildRequires:  emacs-dash
BuildRequires:  emacs-hcl-mode
# /oreon:deps
%description
Major mode of terraform configuration file. terraform-mode provides syntax
highlighting, indentation function and formatting.

Format the current buffer with terraform-format-buffer. To always format
terraform buffers when saving, use:

    (add-hook 'terraform-mode-hook 'terraform-format-on-save-mode)

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pkg}-%{version}

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
