%global source0_hash 36b42ffbe5138ddc56182107c24ad8d6b066ecfd2876829f391e3a4993d89ae1
%global gem_name diffy
Name:          rubygem-%{gem_name}
Version:       3.4.2
Release:        7%{?dist}
Summary:        A convenient way to diff string in ruby
License:       MIT
URL:           http://github.com/samg/diffy
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildArch:     noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
It provides a convenient way to generate a diff from two strings or files.
Instead of reimplementing the LCS diff algorithm Diffy uses battle tested Unix
diff to generate diffs, and focuses on providing a convenient interface,
and getting out of your way.

%package doc
Summary:       Documentation for %{name}
Requires:      %{name} = %{version}-%{release}
BuildArch:     noarch
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
rm -f %{buildroot}%{gem_instdir}/diffy.gemspec
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
  rspec -Ilib spec
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-diffy-doc -f %{oreon_filedir}/rubygem-diffy-doc.list

%changelog

%autochangelog
