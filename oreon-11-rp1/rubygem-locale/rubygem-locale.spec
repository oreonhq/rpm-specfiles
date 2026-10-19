%global source0_hash 1c6803e8aa6bdb2c29e91945d095050601bf6d58474993575adf6f3b89b32ef4
%global	gem_name	locale
Summary:        Pure ruby library which provides basic APIs for localization
Name:		rubygem-%{gem_name}
Version:	2.1.5
Release:        1%{?dist}
License:	(Ruby OR LGPL-3.0-or-later) AND Ruby
URL:		http://ruby-gettext.github.io/
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildArch:	noarch
Requires:	ruby
# oreon:deps
BuildRequires:  ruby
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygem(test-unit-rr)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Ruby-Locale is the pure ruby library which provides basic and general purpose
APIs for localization.
It aims to support all environments which ruby works and all kind of programs
(GUI, WWW, library, etc), and becomes the hub of other i18n/l10n libs/apps to 
handle major locale ID standards. 

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
%description	doc
This package contains documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

# This is needed only on windows
sed -i %{gem_name}-%{version}.gemspec -e '\@runtime.*dependency.*fiddle@d'

%build

gem build %{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/
rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}
rm -rf \
	.yardopts \
	Gemfile \
	Rakefile \
	%{gem_name}.gemspec \
	test/ \
	%{nil}
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
ruby -Ilib:test:. -e 'require "test-unit" ; require "test/unit/rr" ; Dir.glob("test/test_*.rb").each {|f| require f}'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-locale-doc -f %{oreon_filedir}/rubygem-locale-doc.list

%changelog

%autochangelog
