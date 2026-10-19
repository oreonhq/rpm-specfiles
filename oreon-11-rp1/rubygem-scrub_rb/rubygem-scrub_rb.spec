%global source0_hash 7d346064704379f9e793f926680b01901e99e3898bcd24635427f081f8188f37
%global	gem_name	scrub_rb
Name:		rubygem-%{gem_name}
Version:	1.0.1
Release:        23%{?dist}
Summary:        Pure-ruby polyfill of MRI 2.1 String#scrub
License:	MIT
URL:		https://github.com/jrochkind/scrub_rb
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildArch:	noarch
# oreon:deps
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
This gem provides a pure-ruby implementation of 
`String#scrub` and `#scrub!`, monkey-patched into
String, that should work on any ruby platform. 

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build

gem build %{gem_name}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/
pushd %{buildroot}%{gem_instdir}
rm -rf \
	.gitignore .travis.yml \
	Gemfile \
	Rakefile \
	*spec \
	benchmark/ \
	test/
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
sed -i -e "2i gem 'minitest', '~> 4'" \
	test/*_test.rb
ruby -Ilib:. -e \
	"Dir.glob('test/*_test.rb').each {|f| require f}" \
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-scrub_rb-doc -f %{oreon_filedir}/rubygem-scrub_rb-doc.list

%changelog

%autochangelog
