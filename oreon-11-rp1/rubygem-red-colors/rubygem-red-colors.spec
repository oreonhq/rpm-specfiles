%global source0_hash 2356eba0782ca6c44caa47645fbf942a2b16d85905c35c6e3f80d5ff0c04929a
%global gem_name red-colors
Name:		rubygem-%{gem_name}
Version:	0.4.0
Release:        1%{?dist}
Summary:        Red Colors provides a wide array of features for dealing with colors
License:	MIT
URL:		https://github.com/red-data-tools/red-colors
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildArch:	noarch
Requires:		rubygem(json)
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(matrix)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Red Colors provides a wide array of features for dealing with colors. This
includes conversion between colorspaces, desaturation, and parsing colors.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch
%description	doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

%build

gem build %{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/
rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}/
rm -rf \
	.yardopts \
	Gemfile \
	Rakefile \
	*.gemspec \
	test/ \
	%{nil}
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
ruby test/run.rb
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-red-colors-doc -f %{oreon_filedir}/rubygem-red-colors-doc.list

%changelog

%autochangelog
