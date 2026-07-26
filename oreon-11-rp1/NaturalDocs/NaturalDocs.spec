%global source0_hash 3f13c99e15778afe6c5555084a083f856e93567b31b08acd1fd81afb10082681

Name:           NaturalDocs
Version:        1.52
Release:        36%{?dist}
Summary:        Documentation generator for multiple programming languages

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.naturaldocs.org/
Source0:        http://downloads.sourceforge.net/naturaldocs/%{name}-%{version}.zip
Patch0:         NaturalDocs-1.4-paths.patch
BuildArch:      noarch

BuildRequires:  dos2unix
BuildRequires:  perl-generators

%description
Natural Docs is an open-source documentation generator for multiple
programming languages.  You document your code in a natural syntax that
reads like plain English.  Natural Docs then scans your code and builds
high-quality HTML documentation from it.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c
%patch -P0 -p0

%build
# There's a couple of files with DOS line endings
find . -type f -exec dos2unix -q -k '{}' \;

# Convert non-UTF8 files
iconv -f ISO-8859-1 -t UTF-8 Help/example/Default.css >Help/example/Default.css.utf8
touch --reference Help/example/Default.css Help/example/Default.css.utf8
mv Help/example/Default.css.utf8 Help/example/Default.css

iconv -f ISO-8859-1 -t UTF-8 Help/example/Roman.css >Help/example/Roman.css.utf8
touch --reference Help/example/Roman.css Help/example/Roman.css.utf8
mv Help/example/Roman.css.utf8 Help/example/Roman.css

iconv -f ISO-8859-1 -t UTF-8 Help/example/Small.css >Help/example/Small.css.utf8
touch --reference Help/example/Small.css Help/example/Small.css.utf8
mv Help/example/Small.css.utf8 Help/example/Small.css

iconv -f ISO-8859-1 -t UTF-8 License.txt >License.txt.utf8
touch --reference License.txt License.txt.utf8
mv License.txt.utf8 License.txt

# Drop an extra backup file
rm -f Modules/NaturalDocs/Settings.pm.orig

%install
# Directory structure
install -d %{buildroot}%{_datadir}/NaturalDocs
install -d %{buildroot}%{_sysconfdir}/NaturalDocs
install -d %{buildroot}%{perl_vendorlib}
install -d %{buildroot}%{_bindir}

# Copy files
cp -rp Info JavaScript Styles %{buildroot}%{_datadir}/NaturalDocs
cp -rp Modules/* %{buildroot}%{perl_vendorlib}
cp -rp Config/* %{buildroot}%{_sysconfdir}/NaturalDocs
install -pm 755 NaturalDocs %{buildroot}%{_bindir}

%files
%{_datadir}/NaturalDocs
%config(noreplace) %{_sysconfdir}/NaturalDocs
%{perl_vendorlib}/*
%{_bindir}/NaturalDocs
%doc License.txt
%doc Help/*

%changelog
%autochangelog
