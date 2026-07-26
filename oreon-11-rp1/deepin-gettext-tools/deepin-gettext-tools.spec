%global source0_hash f6b8ff0e7853a12b3ba51869df5023caf0d7acc948bb7b5edd9f7c94998c1878

Name:           deepin-gettext-tools
Version:        1.0.11
Release:        %autorelease
Summary:        Translation file processing utils for DDE development
License:        GPL-2.0-or-later
URL:            https://github.com/linuxdeepin/deepin-gettext-tools
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

# for testing
BuildRequires:  python3-devel
BuildRequires:  perl(Config::Tiny)
BuildRequires:  perl(Exporter::Tiny)
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(XML::LibXML::PrettyPrint)

Requires:       gettext
Requires:       qt5-linguist
Requires:       perl(Config::Tiny)
Requires:       perl(Exporter::Tiny)
Requires:       perl(XML::LibXML)
Requires:       perl(XML::LibXML::PrettyPrint)

%description
The tools of gettext function wrapper.

desktop-ts-convert - handling desktop file translations.
policy-ts-convert - convert PolicyKit Policy file to the ts file.
update-pot - scan msgid and generate pot file according to the ini file.
generate-mo - scan po files and generate mo files according to the ini file.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# fix shebang
find -iname "*.py" | xargs sed -i '1s|.*|#!%{__python3}|'
sed -i '1s|.*|#!%{__perl}|' src/desktop_ts_convert.pl

sed -i 's|sudo cp|cp|' src/generate_mo.py
sed -i 's|lconvert|lconvert-qt5|; s|deepin-lupdate|lupdate-qt5|' src/update_pot.py

%build

%install
install -d %{buildroot}%{_bindir}
install -m755 src/desktop_ts_convert.pl %{buildroot}%{_bindir}/deepin-desktop-ts-convert
install -m755 src/policy_ts_convert.py %{buildroot}%{_bindir}/deepin-policy-ts-convert
install -m755 src/generate_mo.py %{buildroot}%{_bindir}/deepin-generate-mo
install -m755 src/update_pot.py %{buildroot}%{_bindir}/deepin-update-pot

%check
/bin/perl src/desktop_ts_convert.pl --help
/bin/python3 src/generate_mo.py --help
/bin/python3 src/update_pot.py --help

%files
%doc README.md
%license LICENSE
%{_bindir}/deepin-desktop-ts-convert
%{_bindir}/deepin-policy-ts-convert
%{_bindir}/deepin-update-pot
%{_bindir}/deepin-generate-mo

%changelog
%autochangelog
