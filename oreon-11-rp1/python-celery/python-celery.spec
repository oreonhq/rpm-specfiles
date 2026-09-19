%global source0_hash none

Name:           python-celery
Version:        5.6.3
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Distributed Task Queue.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://docs.celeryq.dev/en/stable/
Source:         %{pypi_source celery}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'celery' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-celery
Summary:        %{summary}

%description -n python3-celery %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-celery arangodb,auth,azureblockblob,brotli,cassandra,consul,cosmosdbsql,couchbase,couchdb,django,dynamodb,elasticsearch,eventlet,gcs,gevent,librabbitmq,memcache,mongodb,msgpack,pydantic,pymemcache,pyro,pytest,redis,s3,slmq,solar,sqlalchemy,sqs,tblib,yaml,zookeeper,zstd


%prep
%autosetup -p1 -n celery-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x arangodb,auth,azureblockblob,brotli,cassandra,consul,cosmosdbsql,couchbase,couchdb,django,dynamodb,elasticsearch,eventlet,gcs,gevent,librabbitmq,memcache,mongodb,msgpack,pydantic,pymemcache,pyro,pytest,redis,s3,slmq,solar,sqlalchemy,sqs,tblib,yaml,zookeeper,zstd


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-celery -f %{pyproject_files}
%{_bindir}/celery

%changelog
%autochangelog
