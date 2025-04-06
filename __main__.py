"""Creates simple infrastructure for Pulumi import testing."""

import pulumi
import pulumi_oci
import oci

# Parse values from config files
# TO-DO: (add fallback to environment variables)
# Prefix to make distinction between values derived from OCI vs Pulumi config
oci_config = oci.config.from_file(profile_name='TERRAFORM')
compartment_id = oci_config.get('tenancy')
namespace = oci_config.get('namespace')

# Create an OCI Object Storage bucket
bucket = pulumi_oci.objectstorage.Bucket('pulumi-resource-import-bucket',
    compartment_id=compartment_id,
    name='pulumi-resource-import-bucket',
    namespace=namespace,
    metadata={
        'Created-By': 'Pulumi',
        'Purpose': 'Demo'
    },
    storage_tier='Standard',
    versioning='Enabled'
)


pulumi.export('bucket_name', bucket.name)
pulumi.export('bucket_namespace', bucket.namespace)
