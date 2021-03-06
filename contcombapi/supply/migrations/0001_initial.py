# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Fuel'
        db.create_table('fuel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'supply', ['Fuel'])

        # Adding model 'Supply'
        db.create_table('supply', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('vehicle', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vehicle.Vehicle'])),
            ('odometer', self.gf('django.db.models.fields.FloatField')()),
            ('is_full', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('liters', self.gf('django.db.models.fields.FloatField')()),
            ('station', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('fuel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['supply.Fuel'])),
            ('total_spending', self.gf('django.db.models.fields.FloatField')()),
            ('fuel_price', self.gf('django.db.models.fields.FloatField')()),
            ('obs', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'supply', ['Supply'])


    def backwards(self, orm):
        # Deleting model 'Fuel'
        db.delete_table('fuel')

        # Deleting model 'Supply'
        db.delete_table('supply')


    models = {
        u'supply.fuel': {
            'Meta': {'object_name': 'Fuel', 'db_table': "'fuel'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'supply.supply': {
            'Meta': {'object_name': 'Supply', 'db_table': "'supply'"},
            'date': ('django.db.models.fields.DateField', [], {}),
            'fuel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['supply.Fuel']"}),
            'fuel_price': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_full': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'liters': ('django.db.models.fields.FloatField', [], {}),
            'obs': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'odometer': ('django.db.models.fields.FloatField', [], {}),
            'station': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'total_spending': ('django.db.models.fields.FloatField', [], {}),
            'vehicle': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vehicle.Vehicle']"})
        },
        u'user.user': {
            'Meta': {'object_name': 'User', 'db_table': "'user'"},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "'id_user'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'vehicle.mark': {
            'Meta': {'object_name': 'Mark', 'db_table': "'mark'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'vehicle.model': {
            'Meta': {'object_name': 'Model', 'db_table': "'model'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mark': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vehicle.Mark']", 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'valid': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'vehicle.vehicle': {
            'Meta': {'object_name': 'Vehicle', 'db_table': "'vehicle'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manufactured': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'model': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vehicle.Model']", 'null': 'True'}),
            'motor': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['user.User']"})
        }
    }

    complete_apps = ['supply']