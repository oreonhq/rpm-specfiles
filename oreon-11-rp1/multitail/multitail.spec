%global source0_hash b0c92bf5f504b39591bf3e2e30a1902925c11556e14b89a07cfa7533f9bd171b

Name:		multitail
Version:	7.1.5
Release:	%autorelease
Summary:	View one or multiple files like tail but with multiple windows

License:	MIT
URL:		https://www.vanheusden.com/multitail/
Source0:	https://github.com/folkertvanheusden/multitail/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	gcc
BuildRequires:	ncurses-devel

%description
MultiTail lets you view one or multiple files like the original tail
program. The difference is that it creates multiple windows on your
console (with ncurses). It can also monitor wildcards: if another file
matching the wildcard has a more recent modification date, it will
automatically switch to that file. That way you can, for example,
monitor a complete directory of files. Merging of 2 or even more
logfiles is possible.

It can also use colors while displaying the logfiles (through regular
expressions), for faster recognition of what is important and what not.
Multitail can also filter lines (again with regular expressions) and
has interactive menus for editing given regular expressions and
deleting and adding windows. One can also have windows with the output
of shell scripts and other software. When viewing the output of 
external software, MultiTail can mimic the functionality of tools like
'watch' and such.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
# Let rpm handle the config file
sed -i '/multitail.conf.new/d' CMakeLists.txt
# Install conversion-scripts manually
sed -i '/conversion-scripts/d' CMakeLists.txt
# Only build cmake version
rm GNUmakefile

%build
%cmake
%cmake_build

%install
%cmake_install
# Create necessary directorie
mkdir -p %{buildroot}%{_sysconfdir}
install -p -m 644 multitail.conf %{buildroot}%{_sysconfdir}/multitail.conf

# remove documentation later catched up by %%doc
rm -rf %{buildroot}%{_docdir}/

%files
%license LICENSE
%doc manual*.html README.md
%doc conversion-scripts/colors-example.* conversion-scripts/convert-geoip.pl
%doc conversion-scripts/convert-simple.pl
%config(noreplace) %{_sysconfdir}/multitail.conf
%{_bindir}/multitail
%{_mandir}/man1/multitail.1*

%changelog
%autochangelog
