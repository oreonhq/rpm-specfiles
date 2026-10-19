%global source0_hash 8abd4f906cc644aa39bf879f28ec9a0267452342c5689d6c75f40336655c56f8
%global gem_name introspection
Name: rubygem-%{gem_name}
Version: 0.0.4
Release:        1%{?dist}
Summary:        Dynamic inspection of the hierarchy of method definitions on a Ruby object
License: MIT
URL: http://jamesmead.org
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(metaclass)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Dynamic inspection of the hierarchy of method definitions on a Ruby object.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -T
%gem_install -n %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
sed -i '/bundler\/setup/ s/^/#/' test/test_helper.rb
sed -i -e '/require.*blankslate/ s/^/#/' \
  -e '/def test_should_cope_with_blankslate_object$/a\\    skip' \
  test/snapshot_test.rb
ruby -Ilib:test -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-introspection-doc -f %{oreon_filedir}/rubygem-introspection-doc.list

%changelog

%autochangelog
