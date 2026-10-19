%global source0_hash 8746ed10be7e8d305b6be8eb1589fcd3d193f3706cc617ec26de297c86fe07bc
%global gem_name ejs
Name: rubygem-%{gem_name}
Version: 1.1.1
Release:        24%{?dist}
Summary:        EJS (Embedded JavaScript) template compiler
License: MIT
URL: https://github.com/sstephenson/ruby-ejs/
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: %{gem_name}-%{version}-tests.tgz
BuildArch: noarch
# oreon:deps
BuildRequires:  /usr/bin/node
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(execjs)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Compile and evaluate EJS (Embedded JavaScript) templates from Ruby.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
tar xzf %{SOURCE1}
ruby -Ilib -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-ejs-doc -f %{oreon_filedir}/rubygem-ejs-doc.list

%changelog

%autochangelog
