%global source1_hash a7fceebea07d691c061cdbe0da260413d7b590bac2c2e0908087ca93716ffd14
%global source0_hash 11338a9834b207a6989826bb3d9c5505a339dcd3eacbcf8b389598b3ebbcb654
%global gem_name rmail
Name: rubygem-%{gem_name}
Version: 1.1.4
Release:        1%{?dist}
Summary:        A MIME mail parsing and generation library
License: LicenseRef-Callaway-BSD
URL: https://github.com/terceiro/rmail
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://raw.githubusercontent.com/terceiro/rmail/v%{version}/LICENSE
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
RMail is a lightweight mail library containing various utility classes and
modules that allow ruby scripts to parse, modify, and generate MIME mail
messages.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
cp -p %{SOURCE1} .

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
for file in `find %{buildroot}/%{gem_instdir} -type f ! -perm /a+x -name "*.rb"`; do
    [ ! -z "`head -n 1 $file | grep \"^#!/\"`" ] && sed -i -e '/^#!\//, 1d' $file
done
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
ruby -I. -Ilib -e 'Dir.glob "./test/test*.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-rmail-doc -f %{oreon_filedir}/rubygem-rmail-doc.list

%changelog

%autochangelog
