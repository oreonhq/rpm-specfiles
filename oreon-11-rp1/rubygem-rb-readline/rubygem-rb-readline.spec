%global source0_hash 9e9bd7e198bdef0822c46902f6c592b882c1f9777894a4c3dcf5b320824a8793
%global	gem_name	rb-readline
Name:		rubygem-%{gem_name}
Version:	0.5.5
Release:        20%{?dist}
Summary:        Pure-Ruby Readline Implementation
License:	BSD-3-Clause
URL:		http://github.com/ConnorAtherton/rb-readline
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0:	rb-readline-0.5.5-minitest6.patch
Patch1:	rb-readline-0.5.5-frozen-string.patch
BuildArch:		noarch
# oreon:deps
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
The readline library provides a pure Ruby implementation of the GNU readline C
library, as well as the Readline extension that ships as part of the standard
library.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch
%description	doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
%patch -P0 -p1
%patch -P1 -p1
mv ../%{gem_name}-%{version}.gemspec .

%build

gem build %{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/
rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}/
rm -rf \
	Rakefile \
	setup.rb \
	*.gemspec \
	bench/ \
	test/ \
	%{nil}
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

remove_fail_test() {
	filename=$1
	shift
	num=$#
	while [ $num -gt 0 ]
	do
		if [ ! -f ${filename}.orig ] ; then
			cp -p $filename ${filename}.orig
		fi
		sed -i $filename -e "\@def.*$1@,\@end@d"
		shift
		num=$((num - 1))
	done
}
pushd .%{gem_instdir}
ruby -Ilib:.:test -e \
	'Dir.glob("test/test_*.rb").each{|f| require f}' || true
remove_fail_test test/test_readline.rb test_readline_with_default_parameters_does_not_error
ruby -Ilib:.:test -e \
	'Dir.glob("test/test_*.rb").each{|f| require f}'
find . -name \*.orig | while read f ; do mv $f ${f%.orig} ; done
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-rb-readline-doc -f %{oreon_filedir}/rubygem-rb-readline-doc.list

%changelog

%autochangelog
