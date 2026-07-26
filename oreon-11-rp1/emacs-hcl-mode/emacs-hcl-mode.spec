%global source0_hash dd4cd40a4dced593a6eb0716bb60b8ed682c3b27d76b733fb61f407e31397c5f

%global pkg hcl-mode

Name:           emacs-%{pkg}
Version:        0.03
Release:        17%{?dist}
Summary:        Emacs major mode of HCL (Hashicorp Configuration Language)

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/syohex/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{pkg}-init.el

BuildRequires:  emacs
Requires:       emacs(bin) >= %{_emacs_version}
BuildArch:      noarch

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%{_emacs_bytecompile} %{pkg}.el

%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 %{pkg}.el* -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/

install -Dpm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_emacs_sitestartdir}/%{pkg}-init.el

%check
emacs --batch -q --no-site-file --no-splash \
    -L $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/ \
    -l test/test-command.el \
    -l test/test-helper.el \
    -l test/test-highlighting.el \
    -l test/test-indentation.el \
    -f ert-run-tests-batch-and-exit

%files
%doc Changes README.md
%{_emacs_sitelispdir}/%{pkg}/
%{_emacs_sitestartdir}/*.el

%changelog
%autochangelog
