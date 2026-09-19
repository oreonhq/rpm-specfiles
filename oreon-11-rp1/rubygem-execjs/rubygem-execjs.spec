%global source0_hash 6d939919cfd81bcc4d6556f322c3995a70cfe4289ea0bd3b1f999b489c323088

# Generated from execjs-1.4.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name execjs

Summary: Run JavaScript code from Ruby
Name: rubygem-%{gem_name}
Version: 2.8.1
Release: 12%{?dist}
License: MIT
URL: https://github.com/rails/execjs
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/rails/execjs.git && cd execjs
# git checkout v2.8.1 && tar czf execjs-2.8.1-tests.tgz test/
Source1: %{gem_name}-%{version}-tests.tgz
# Revert f47c02c and 8b22842 fixing conflict to unbundle json2.js.
Patch0: rubygem-execjs-2.7.0-delete-JScript-and-json2.js.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(minitest)
BuildRequires: %{_bindir}/node
BuildArch: noarch

%description
ExecJS lets you run JavaScript code from Ruby. It automatically picks the
best runtime available to evaluate your JavaScript program, then returns
the result to you as a Ruby object.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%patch 0 -p1
sed -i -e '/files/ s|"lib/execjs/support/jscript_runner.js".freeze, ||' \
    -e '/files/ s|"lib/execjs/support/json2.js".freeze, ||' %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
tar xzf %{SOURCE1}
ruby -Ilib -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
