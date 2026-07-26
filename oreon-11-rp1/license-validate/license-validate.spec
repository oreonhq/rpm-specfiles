%global source0_hash 4215b6d4512397bf77295d0473bc0f05e00973982b665b6322b9edb187a82e99

Name:           license-validate
Version:        30
Release:        1%{?dist}
Summary:        Validate SPEC license string

License:        MIT
URL:            https://github.com/fedora-copr/license-validate
# source is created by:
# git clone https://github.com/fedora-copr/license-validate.git
# cd license-validate; tito build --tgz
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

Requires:       python3dist(specfile)
Requires:       fedora-license-data >= 1.18
BuildRequires:  fedora-license-data >= 1.18
BuildRequires:  python3-devel

# man pages
BuildRequires:  asciidoc
BuildRequires:  libxslt

# for test
BuildRequires:  (python3dist(lark) or python3dist(lark-parser))
Requires:       (python3dist(lark) or python3dist(lark-parser))
BuildRequires:  %{py3_dist pytest}
BuildRequires:  python3dist(specfile)

%description
Validate whether the license string conforms to Fedora Licensing.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
./generate-shortnames.py > fedora-shortnames.txt
./create-grammar.py grammar-shortnames.lark fedora-shortnames.txt > full-grammar-shortnames.lark
for i in license-validate.1.asciidoc license-fedora2spdx.asciidoc; do
  a2x -d manpage -f manpage "$i"
done

%install
mkdir -p %{buildroot}%{_bindir}
install license-validate.py %{buildroot}%{_bindir}/license-validate
install license-fedora2spdx.py %{buildroot}%{_bindir}/license-fedora2spdx

mkdir -p %{buildroot}%{_datadir}/%{name}/
install -m644 full-grammar-shortnames.lark %{buildroot}%{_datadir}/%{name}/grammar-shortnames.lark

mkdir -p %{buildroot}%{_mandir}/man1
install -m644 license-validate.1 %{buildroot}/%{_mandir}/man1/
install -m644 license-fedora2spdx.1 %{buildroot}/%{_mandir}/man1/

%check
./validate-grammar.py full-grammar-shortnames.lark
%{pytest} test_license.py

%files
%license LICENSE
%doc README.md
%{_bindir}/license-validate
%{_bindir}/license-fedora2spdx
%{_datadir}/%{name}
%doc %{_mandir}/man1/license-validate.1*
%doc %{_mandir}/man1/license-fedora2spdx.1*

%changelog
%autochangelog
