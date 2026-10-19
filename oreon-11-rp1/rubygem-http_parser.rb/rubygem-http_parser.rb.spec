%global source0_hash 5a0932f1fa82ce08a8516a2685d5a86031c000560f89946913c555a0697544be
%global gem_name http_parser.rb
Name:		rubygem-%{gem_name}
Version:	0.8.0
Release:        11%{?dist}
Summary:        Simple callback-based HTTP request/response parser
License:	MIT
URL:		https://github.com/tmm1/http_parser.rb
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0:	http_parser.rb-pr86-ruby35-Ractor-change.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  ruby-devel
BuildRequires:  rubygem-rspec
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Ruby bindings to http://github.com/joylent/http-parser and
http://github.com/a2800276/http-parser.java.

%package doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gem_name}-%{version} -p1

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{gem_extdir_mri}/lib
cp -ar .%{gem_instdir}/lib/ruby_http_parser.so %{buildroot}%{gem_extdir_mri}/lib
rm -rf %{buildroot}%{gem_instdir}/{ext/,.github/}
rm -f %{buildroot}%{gem_instdir}/{.gitignore,.gitmodules,Gemfile.lock}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
rspec -Ilib -I%{buildroot}%{gem_extdir_mri} spec
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-http_parser.rb-doc -f %{oreon_filedir}/rubygem-http_parser.rb-doc.list

%changelog

%autochangelog
