%global source0_hash 11338a9834b207a6989826bb3d9c5505a339dcd3eacbcf8b389598b3ebbcb654

# Generated from rmail-1.1.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name rmail

Name: rubygem-%{gem_name}
Version: 1.1.4
Release: 14%{?dist}
Summary: A MIME mail parsing and generation library
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL: https://github.com/terceiro/rmail
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# LICENSE is in the source tree but is not included in the gem
Source1: https://raw.githubusercontent.com/terceiro/rmail/v%{version}/LICENSE
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 1.8.1
BuildRequires: rubygem(test-unit)
BuildArch: noarch

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
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# Remove shebang from files that do not have executable permissions
for file in `find %{buildroot}/%{gem_instdir} -type f ! -perm /a+x -name "*.rb"`; do
    [ ! -z "`head -n 1 $file | grep \"^#!/\"`" ] && sed -i -e '/^#!\//, 1d' $file
done

%check
pushd .%{gem_instdir}
ruby -I. -Ilib -e 'Dir.glob "./test/test*.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%license LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/ChangeLog
%doc %{gem_instdir}/NOTES
%doc %{gem_instdir}/THANKS
%doc %{gem_instdir}/TODO
%doc %{gem_instdir}/guide
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
%autochangelog
