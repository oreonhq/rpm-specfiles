%global source0_hash a1df037310624ecc1ea1d81264b11c83e96d0c3c1c6043108d37d396dcd0f4b1
%global gem_name open4
Summary:        Manage child processes and their IO handles easily
Name: rubygem-%{gem_name}
Version: 1.3.4
Release:        1%{?dist}
License: LicenseRef-Callaway-BSD OR Ruby
URL: http://github.com/ahoward/open4/
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0:  open4-pr32-minitest-5_19-compat.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Open child process with handles on pid, stdin, stdout, and stderr.
Manage child processes and their IO handles easily.

%package doc
Summary: Documentation for %{name}
Requires:%{name} = %{version}-%{release}
%description doc
Documentation for %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
%patch -P0 -p1

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
sed -i '/#!.*env ruby/d' %{buildroot}%{gem_instdir}/samples/jesse-caldwell.rb
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
ruby -Ilib:test/lib -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-open4-doc -f %{oreon_filedir}/rubygem-open4-doc.list

%changelog

%autochangelog
