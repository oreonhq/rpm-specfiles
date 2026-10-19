%global source0_hash dd4cd40a4dced593a6eb0716bb60b8ed682c3b27d76b733fb61f407e31397c5f
%global pkg hcl-mode
Name:           emacs-%{pkg}
Version:        0.03
Release:        1%{?dist}
Summary:        Emacs major mode of HCL (Hashicorp Configuration Language)
License:        GPL-3.0-or-later
URL:            https://github.com/syohex/%{name}
Source0:        https://github.com/syohex/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{pkg}-init.el
Requires:       emacs(bin) >= %{_emacs_version}
BuildArch:      noarch
# oreon:deps
BuildRequires:  emacs
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
install -Dpm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_emacs_sitestartdir}/%{pkg}-init.el
%oreon_autofiles main

%check

emacs --batch -q --no-site-file --no-splash \
    -L $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/ \
    -l test/test-command.el \
    -l test/test-helper.el \
    -l test/test-highlighting.el \
    -l test/test-indentation.el \
    -f ert-run-tests-batch-and-exit
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
